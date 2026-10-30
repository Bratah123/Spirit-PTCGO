"""STUB: effect not implemented — do not guess mechanics.
Minun (EX5 #67): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


from spirit.game.card_effects.ex import minus_energy

card = PokemonCardDef(
    guid="a25b7ab3-0c2f-517a-afe1-560dfff354ae",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name",
    display_name="Minun",
    searchable_by=["Minun", "Basic", "Minun"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="EX5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=312,
    abilities=[
        Attack(
            title="Minus Energy",
            game_text="Flip a coin. If heads, choose 1 Energy attached to the Defending Pok\u00e9mon. Your opponent returns that card to his or her hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=minus_energy(),
        ),
        Attack(
            title="Thundershock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)