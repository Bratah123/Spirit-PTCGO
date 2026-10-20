from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_random_from_hand
from spirit.game.card_effects.passives_common import ability_lock_passive
from spirit.game.content.definitions import def_for


async def knock_off(ctx):
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=1)


def _is_break(pokemon, carrier):
    return "BREAK" in (getattr(def_for(pokemon.archetype_id), "subtypes", None) or [])


card = PokemonCardDef(
    guid="34c29038-3972-54d1-99d0-c44a1c2258e2",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name",
    display_name="Giratina",
    searchable_by=["Giratina", "Basic", "Giratina"],
    subtypes=["Basic"],
    collector_number=184,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=487,
    abilities=[
        Ability(
            title="Devour Light",
            game_text="Each Pok\u00e9mon BREAK has no Abilities (this includes Abilities of its previous Evolution).",
            passive=ability_lock_passive(_is_break),
        ),
        Attack(
            title="Shadow Claw",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=knock_off,
        ),
    ],
)