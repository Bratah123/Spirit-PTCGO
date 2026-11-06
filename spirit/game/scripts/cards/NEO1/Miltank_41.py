from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import milk_drink


card = PokemonCardDef(
    guid="eacfec8d-cb32-5c17-a31e-642a0b5e25d1",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name",
    display_name="Miltank",
    searchable_by=["Miltank", "Basic", "Miltank"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=241,
    abilities=[
        Attack(
            title="Milk Drink",
            game_text="Flip 2 coins. Remove 2 damage counters times the number of heads from Miltank. If it has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=milk_drink,
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
