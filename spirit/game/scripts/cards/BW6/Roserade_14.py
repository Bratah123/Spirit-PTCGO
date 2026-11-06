from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage


card = PokemonCardDef(
    guid="433768bf-693d-58cc-9f3b-895040efadab",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name",
    display_name="Roserade",
    searchable_by=["Roserade", "Stage 1", "Roserade"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    family_id=315,
    abilities=[
        Attack(
            title="Crosswise Whip",
            game_text="Flip 4 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(4, per_heads=30),
        ),
        Attack(
            title="Poison Point",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)