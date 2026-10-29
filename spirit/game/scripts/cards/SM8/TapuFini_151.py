from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

from spirit.game.card_effects.sm8 import (
    dream_away,
)

card = PokemonCardDef(
    guid="348d9ffc-2d1f-5fdb-9d58-3dbbd89690c1",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuFini.Name",
    display_name="Tapu Fini",
    searchable_by=["Tapu Fini", "Basic", "TapuFini"],
    subtypes=["Basic"],
    collector_number=151,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=788,
    abilities=[
        Attack(
            title="Dream Away",
            game_text="Flip a coin. If heads, your opponent shuffles their Active Pok\u00e9mon and all cards attached to it into their deck.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            effect=dream_away
        ),
        Attack(
            title="Wonder Shine",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)