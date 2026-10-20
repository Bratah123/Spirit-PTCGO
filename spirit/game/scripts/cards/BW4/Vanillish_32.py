from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="7c49bf3f-abbc-5a01-92db-e82004ffacb9",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    display_name="Vanillish",
    searchable_by=["Vanillish", "Stage 1", "Vanillish"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Icy Wind",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
    ],
)