from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import debuff_defender_attacks
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_dark_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.DARKNESS.value)


async def _dark_burn(ctx):
    """Discard any number of Darkness Energy attached to your Pokemon; 50x that many."""
    pool = [e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p) if _is_dark_energy(e)]
    picked = await ctx.choose_cards(pool, len(pool), minimum=0, prompt="Discard any Darkness Energy") if pool else []
    if picked:
        await ctx.discard_cards(picked)
    await ctx.deal_damage(50 * len(picked))


card = PokemonCardDef(
    guid="40fc8638-9dda-53c6-9000-0550b1a8eef6",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=86,
    set_code="XY11",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Cruel Fang",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 40 (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=debuff_defender_attacks(40),
        ),
        Attack(
            title="Dark Burn",
            game_text="Discard as many Darkness Energy attached to your Pok\u00e9mon as you like. This attack does 50 damage times the amount of Darkness Energy you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=_dark_burn,
        ),
    ],
)