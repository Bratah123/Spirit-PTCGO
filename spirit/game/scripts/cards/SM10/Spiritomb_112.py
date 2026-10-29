from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    anguish_cry,
    building_spite,
)

card = PokemonCardDef(
    guid="c1ebf1a3-23d0-5f5e-bdc6-be1feb50ebe8",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=442,
    abilities=[
        Ability(
            title="Building Spite",
            game_text="Once during your turn (before your attack), you may put 1 damage counter on this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            effect=building_spite
        ),
        Attack(
            title="Anguish Cry",
            game_text="This attack does 30 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="+",
            effect=anguish_cry
        ),
    ],
)