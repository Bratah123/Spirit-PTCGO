"""STUB: effect not implemented — do not guess mechanics.
Sudowoodo (EX10 #15): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import karate_chop, copy_defending_attack

card = PokemonCardDef(
    guid="950ad2e1-8a70-5c4c-8228-b940b52c2b26",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=185,
    abilities=[
        Attack(
            title="Copy",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. Copy copies that attack. This attack does nothing if Sudowoodo doesn't have the Energy necessary to use that attack. (You must still do anything else required for that attack.) Sudowoodo performs that attack.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=copy_defending_attack(),
        ),
        Attack(
            title="Karate Chop",
            game_text="Does 50 damage minus 10 damage for each damage counter on Sudowoodo.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="-",
            effect=karate_chop(50, 10),
        ),
    ],
)