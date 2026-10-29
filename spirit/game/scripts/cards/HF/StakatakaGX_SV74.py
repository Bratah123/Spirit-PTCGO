from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm7 import (
    assembly_gx,
    ultra_wall_passive,
)

card = PokemonCardDef(
    guid="63696928-845d-56df-83fc-ccbd3d93f001",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StakatakaGX.Name",
    display_name="Stakataka-GX",
    searchable_by=["Stakataka-GX", "Basic", "GX", "Ultra Beast", "StakatakaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=143,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=805,
    abilities=[
        Ability(
            title="Ultra Wall",
            game_text="Your Ultra Beasts take 10 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=ultra_wall_passive,
        ),
        Attack(
            title="Gigaton Stomp",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title="Assembly-GX",
            game_text="This attack does 50 more damage for each Prize card you have taken. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=assembly_gx,
        ),
    ],
)