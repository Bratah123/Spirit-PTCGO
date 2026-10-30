from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="8c2fbe45-5748-513e-8f9f-bbb919ac17c9",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    display_name="Ivysaur",
    searchable_by=["Ivysaur", "Stage 1", "Ivysaur"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    family_id=1,
    abilities=[
        Attack(
            title="Poison Seed",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)