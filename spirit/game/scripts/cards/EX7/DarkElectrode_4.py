from spirit.game.card_effects.ex import darkness_navigation, energy_bomb_redistribute
"""STUB: effect not implemented — do not guess mechanics.
Dark Electrode (EX7 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="2c16a7c5-8701-59e3-8a23-c6d70c141765",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkElectrode.Name",
    display_name="Dark Electrode",
    searchable_by=["Dark Electrode", "Stage 1", "DarkElectrode"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Ability(
            title="Darkness Navigation",
            game_text="Once during your turn (before your attack), if Dark Electrode has no Energy attached to it, you may search your deck for a Darkness or Dark Metal Energy and attach it to Dark Electrode. Shuffle your deck afterward. This power can't be used if Dark Electrode is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=darkness_navigation(),
        ),
        Attack(
            title="Energy Bomb",
            game_text="You may move all Energy cards attached to Dark Electrode to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=energy_bomb_redistribute(),
        ),
    ],
)