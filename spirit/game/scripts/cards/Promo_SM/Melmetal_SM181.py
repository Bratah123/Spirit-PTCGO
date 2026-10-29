from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    metal_eater,
    metal_eater_condition,
)

card = PokemonCardDef(
    guid="1905b3fa-50aa-5e63-bd80-e75b320a91d1",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Melmetal.Name",
    display_name="Melmetal",
    searchable_by=["Melmetal", "Stage 1", "Melmetal"],
    subtypes=["Stage 1"],
    collector_number=181,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=808,
    abilities=[
        Ability(
            title="Metal Eater",
            game_text="Once during your turn (before your attack), you may discard a Metal Pok\u00e9mon from your hand. If you do, heal 100 damage from this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=metal_eater_condition,
            effect=metal_eater
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)