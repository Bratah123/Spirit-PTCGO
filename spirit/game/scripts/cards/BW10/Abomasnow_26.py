from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="dc745a5c-b86c-50e0-8fb8-a53afcb216f1",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name",
    display_name="Abomasnow",
    searchable_by=["Abomasnow", "Stage 1", "Abomasnow"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    family_id=459,
    abilities=[
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
        ),
        Attack(
            title="Bang Heads",
            game_text="Both this Pok\u00e9mon and the Defending Pok\u00e9mon are now Confused.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=condition_attack(SpecialConditions.CONFUSED, self_conditions=(SpecialConditions.CONFUSED,)),
        ),
    ],
)