from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.passives_common import team_damage_boost_passive
from spirit.game.card_effects.attacks_common import lock_all_attacks


async def max_thunder_and_lightning(ctx):
    """220. During your next turn, this Pokémon can't attack."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="34ebe757-910b-56f2-bd70-acfcd01ddd68",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegielekiVMAX.Name",
    display_name="Regieleki VMAX",
    searchable_by=["Regieleki VMAX", "VMAX", "RegielekiVMAX"],
    subtypes=["VMAX"],
    collector_number=198,
    set_code="SWSH12",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RegielekiV.Name",
    family_id=894,
    abilities=[
        Ability(
            title="Transistor",
            game_text="Your Basic Lightning Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(
                30,
                attacker_pred=lambda p: is_basic_pokemon(p) and PokemonTypes.LIGHTNING.value in (
                    p.get_attribute(AttrID.POKEMON_TYPES) or []),
            ),
        ),
        Attack(
            title="Max Thunder and Lightning",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=220,
            effect=max_thunder_and_lightning,
        ),
    ],
)