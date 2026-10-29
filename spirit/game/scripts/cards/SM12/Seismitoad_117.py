from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import tremulous_fist
from spirit.game.card_effects.sm7 import deck_has_cards, smooth_over
from spirit.game.data_utils import Activations


card = PokemonCardDef(
    guid="efcf3d74-4c16-5430-8be9-b5bd24a30fcc",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=["Seismitoad", "Stage 2", "Seismitoad"],
    subtypes=["Stage 2"],
    collector_number=117,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Ability(
            title="Bulldoze",
            game_text="Once during your turn (before your attack), you may search your deck for a card, shuffle your deck, then put that card on top of it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            effect=smooth_over,
            condition=deck_has_cards,
        ),
        Attack(
            title="Tremulous Fist",
            game_text="This attack does 30 more damage for each of your Benched Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=tremulous_fist,
        ),
    ],
)