from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import energy_stream


card = PokemonCardDef(
    guid="2767f0d7-1195-5d21-8445-6fd8872339da",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    display_name="Poliwhirl",
    searchable_by=["Poliwhirl", "Stage 1", "Poliwhirl"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Energy Stream",
            game_text="Search your discard pile for a basic Energy card and attach it to Poliwhirl.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=energy_stream(),
        ),
        Attack(
            title="Bubble",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)