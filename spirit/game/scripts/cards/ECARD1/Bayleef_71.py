from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="395b80e2-7493-5a4a-9b8a-837afb56dd9f",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    display_name="Bayleef",
    searchable_by=["Bayleef", "Stage 1", "Bayleef"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name",
    family_id=152,
    abilities=[
        Attack(
            title="Mysterious Powder",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
