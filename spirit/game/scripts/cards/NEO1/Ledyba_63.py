from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage


card = PokemonCardDef(
    guid="66276b54-7e4e-5a74-8fc9-f5486595a382",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name",
    display_name="Ledyba",
    searchable_by=["Ledyba", "Basic", "Ledyba"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=165,
    abilities=[
        Attack(
            title="Supersonic",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Comet Punch",
            game_text="Flip 4 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 2},
            damage=0,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=10),
        ),
    ],
)
