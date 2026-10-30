"""STUB: effect not implemented — do not guess mechanics.
Electrode (EX5 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import swift_attack
from spirit.game.card_effects.ex import mass_destruction


card = PokemonCardDef(
    guid="719f4084-bc73-5616-a417-a6a5e26af86a",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=swift_attack(),
        ),
        Attack(
            title="Mass Destruction",
            game_text="Both Electrode and the Defending Pok\u00e9mon are now Knocked Out. If Electrode has any Special Energy cards attached to it, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=mass_destruction(),
        ),
    ],
)