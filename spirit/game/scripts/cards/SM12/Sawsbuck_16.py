from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.card_effects.support_common import draw_attack, switch_self_attack
from spirit.game.card_effects.trainers import deck_nonempty


card = PokemonCardDef(
    guid="bde1aa5b-59c7-51c9-8207-186abc447716",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawsbuck.Name",
    display_name="Sawsbuck",
    searchable_by=["Sawsbuck", "Stage 1", "Sawsbuck"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name",
    family_id=585,
    abilities=[
        Ability(
            title="Seasonal Blessings",
            game_text="Once during your turn (before your attack), you may draw a card.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, pokemon=None: deck_nonempty(board, player_id),
            effect=draw_attack(1),
        ),
        Attack(
            title="Bounce",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=switch_self_attack(optional=True),
        ),
    ],
)