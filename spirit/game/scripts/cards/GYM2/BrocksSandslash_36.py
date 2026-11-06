from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import swift
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="966dddc2-4b78-59ac-8d4b-f4c53412b83c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksSandslash.Name",
    display_name="Brock's Sandslash",
    searchable_by=["Brock's Sandslash", "Stage 1", "BrocksSandslash"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksSandshrew.Name",
    family_id=28,
    abilities=[
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9mon Powers, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=swift,
        ),
        Attack(
            title="Needle Ball",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)
