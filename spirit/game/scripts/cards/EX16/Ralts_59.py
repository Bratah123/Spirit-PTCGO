"""STUB: effect not implemented — do not guess mechanics.
Ralts (EX16 #59): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import teleportation_burst_switch
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c0d11f1d-dd13-5602-a23d-8a860a206dac",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    display_name="Ralts",
    searchable_by=["Ralts", "Basic", "Ralts"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="EX16",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=280,
    abilities=[
        Attack(
            title="Slap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Teleportation Burst",
            game_text="Switch Ralts with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=teleportation_burst_switch(),
        ),
    ],
)