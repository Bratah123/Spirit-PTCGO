"""STUB: effect not implemented — do not guess mechanics.
Sharpedo ex (EX8 #104): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import darkness_blast_optional, drag_off_optional_ex8


card = PokemonCardDef(
    guid="f637ef3d-cd7e-53a2-84c1-ca16e740be9f",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedoex.Name",
    display_name="Sharpedo ex",
    searchable_by=["Sharpedo ex", "Stage 1", "ex", "Sharpedoex"],
    subtypes=["Stage 1", "ex"],
    collector_number=104,
    set_code="EX8",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    family_id=318,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Before doing damage, you may switch 1 of your opponent's Benched Pok\u00e9mon with the Defending Pok\u00e9mon. If you do, this attack does 20 damage to the new Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=drag_off_optional_ex8(),
        ),
        Attack(
            title="Darkness Blast",
            game_text="You may discard a Darkness Energy attached to Sharpedo ex. If you do, this attack does 60 damage plus 20 more damage and discard 1 Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=darkness_blast_optional(),
        ),
    ],
)