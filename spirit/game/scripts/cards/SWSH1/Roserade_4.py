from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="683015b9-fae8-5341-aa5d-3c74a1e92f52",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name",
    display_name="Roserade",
    searchable_by=["Roserade", "Stage 1", "Roserade"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    family_id=315,
    abilities=[
        Attack(
            title="Paralyze Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Flip a coin. If heads, your opponent's Active Pok\u00e9mon is also Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=condition_attack(
                SpecialConditions.PARALYZED, flip=True,
                always_conditions=(SpecialConditions.POISONED,),
            ),
        ),
        Attack(
            title="Mega Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=heal_attack(30),
        ),
    ],
)