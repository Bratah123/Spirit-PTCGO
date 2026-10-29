from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm9 import (
    nine_temptations,
    nine_temptations_condition,
)

card = PokemonCardDef(
    guid="78e8fadb-5980-5e90-a120-eeb55a6fe1f7",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Ability(
            title="Nine Temptations",
            game_text="Once during your turn (before your attack), you may discard 2 Fire Energy cards from your hand. If you do, switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=nine_temptations,
            activation=Activations.ONCE_PER_TURN,
            condition=nine_temptations_condition,
        ),
        Attack(
            title="Flame Tail",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)