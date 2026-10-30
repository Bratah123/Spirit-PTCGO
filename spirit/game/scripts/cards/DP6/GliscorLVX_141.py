"""STUB: effect not implemented — do not guess mechanics.
Gliscor LV.X (DP6 #141): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="4bd62747-2043-502e-a5b7-8e081e3046c6",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GliscorLVX.Name",
    display_name="Gliscor LV.X",
    searchable_by=["Gliscor LV.X", "Level-Up", "GliscorLVX"],
    subtypes=["Level-Up"],
    collector_number=141,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.LEVELUP,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name",
    family_id=207,
    abilities=[
        Ability(
            title="Shoot Poison",
            game_text="Once during your turn (before your attack), when you put Gliscor LV.X from your hand onto your Active Gliscor, you may choose 1 of the Defending Pok\u00e9mon. That Pok\u00e9mon is now Paralyzed and Poisoned.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Night Slash",
            game_text="You may switch Gliscor with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)