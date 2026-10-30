from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import white_hot_flame, white_hot_flame_condition


card = PokemonCardDef(
    guid="3d41f97e-f76c-53e7-a980-3f5d25b6fe4e",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningCharizard.Name",
    display_name="Shining Charizard",
    searchable_by=["Shining Charizard", "Basic", "ShiningCharizard"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="NEO4",
    rarity=Rarities.Shining,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=6,
    abilities=[
        Attack(
            title="White-hot Flame",
            game_text="Discard 1 Fire Energy card and 1 Lightning Energy card attached to Shining Charizard or this attack does nothing. Flip a coin. If tails, Shining Charizard does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.LIGHTNING: 2},
            damage=100,
            condition=white_hot_flame_condition,
            effect=white_hot_flame,
        ),
    ],
)
