from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="21589e07-d566-5b8a-a5d9-1c03bc4e8d4e",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasSlowpoke.Name",
    display_name="Sabrina's Slowpoke",
    searchable_by=["Sabrina's Slowpoke", "Basic", "SabrinasSlowpoke"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=79,
    abilities=[
        Attack(
            title="Lazy Attack",
            game_text="Sabrina's Slowpoke is now Asleep (after doing damage).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,)),
        ),
    ],
)
