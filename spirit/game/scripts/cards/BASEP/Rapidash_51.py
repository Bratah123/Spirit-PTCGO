from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import jump_over


card = PokemonCardDef(
    guid="0ea5ba52-18d3-520a-a6d1-8e9d7fb02f98",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rapidash.Name",
    display_name="Rapidash",
    searchable_by=["Rapidash", "Stage 1", "Rapidash"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    family_id=78,
    abilities=[
        Attack(
            title="Jump Over",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them. Flip a coin. If heads, this attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=jump_over,
        ),
        Attack(
            title="Super Singe",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.BURNED, flip=True),
        ),
    ],
)
