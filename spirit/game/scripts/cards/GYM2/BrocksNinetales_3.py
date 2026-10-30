from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    shapeshift, shapeshift_condition, shapeshift_passive,
)


card = PokemonCardDef(
    guid="25b65583-fc0f-5be1-99d5-d355ddc4cd78",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksNinetales.Name",
    display_name="Brock's Ninetales",
    searchable_by=["Brock's Ninetales", "Stage 1", "BrocksNinetales"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksVulpix.Name",
    family_id=37,
    abilities=[
        Ability(
            title="Shapeshift",
            game_text="Once during your turn (before your attack), you may attach an Evolution card from your hand to Brock's Ninetales. (This doesn't count as evolving Brock's Ninetales.) Treat Brock's Ninetales as if it were that Pok\u00e9mon instead. It can't evolve, devolve, or use the Pok\u00e9mon Power of that Pok\u00e9mon. During your turn, you may discard the Evolution card attached to Brock's Ninetales. This power can't be used if Brock's Ninetales is Asleep, Confused, or Paralyzed. If Brock's Ninetales becomes Asleep, Confused, or Paralyzed, discard all Evolution cards attached to it.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.UNLIMITED,
            condition=shapeshift_condition,
            effect=shapeshift,
            passive=shapeshift_passive,
        ),
        Attack(
            title="Will-o'-the-wisp",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
    ],
)
