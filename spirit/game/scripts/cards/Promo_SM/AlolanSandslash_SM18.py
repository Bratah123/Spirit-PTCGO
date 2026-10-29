from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.data_utils import Activations
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.trainers import deck_nonempty


card = PokemonCardDef(
    guid="add2c2e5-4cbf-5502-ae83-55bbc977e92f",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandslash.Name",
    display_name="Alolan Sandslash",
    searchable_by=["Alolan Sandslash", "Stage 1", "AlolanSandslash"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandshrew.Name",
    family_id=27,
    abilities=[
        Ability(
            title="Slush Rush",
            game_text="Once during your turn (before your attack), you may draw a card.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN, condition=lambda board, player_id, pokemon=None: deck_nonempty(board, player_id),
            effect=draw_attack(1),
        ),
        Attack(
            title="Smash Turn",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=switch_self_attack(),
        ),
    ],
)