"""STUB: effect not implemented — do not guess mechanics.
Lugia ex (EX10 #105): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import silver_sparkle_on_damaged_passive, elemental_blast

card = PokemonCardDef(
    guid="725ba406-1d90-5348-a74a-945e609b4c4a",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugiaex.Name",
    display_name="Lugia ex",
    searchable_by=["Lugia ex", "Basic", "ex", "Lugiaex"],
    subtypes=["Basic", "ex"],
    collector_number=105,
    set_code="EX10",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Ability(
            title="Silver Sparkle",
            game_text="If Lugia ex is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Lugia ex is Knocked Out), flip a coin. If heads, choose an Energy card attached to the Attacking Pok\u00e9mon and return it to your opponent's hand.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=silver_sparkle_on_damaged_passive(),
        ),
        Attack(
            title="Elemental Blast",
            game_text="Discard a Fire Energy, Water Energy, and Lightning Energy attached to Lugia ex.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=200,
            # STUB: attack effect not implemented
            effect=elemental_blast(PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.LIGHTNING),
        ),
    ],
)