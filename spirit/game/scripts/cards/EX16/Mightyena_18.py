"""STUB: effect not implemented — do not guess mechanics.
Mightyena (EX16 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import dark_burst_sidney, night_song_gust_asleep


card = PokemonCardDef(
    guid="18660979-b8ec-5293-b986-7dc53924e8a6",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mightyena.Name",
    display_name="Mightyena",
    searchable_by=["Mightyena", "Stage 1", "Mightyena"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="EX16",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    family_id=261,
    abilities=[
        Attack(
            title="Plunder",
            game_text="Before doing damage, discard all Trainer cards attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=night_song_gust_asleep(),
        ),
        Attack(
            title="Dark Burst",
            game_text="If Sidney's Stadium is in play, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=dark_burst_sidney(50, 20),
        ),
    ],
)