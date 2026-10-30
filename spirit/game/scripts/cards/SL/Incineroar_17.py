"""STUB: effect not implemented — do not guess mechanics.
Incineroar (SL #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, self_energy_discard_attack
from spirit.game.card_effects.sl import bench_has_damage


card = PokemonCardDef(
    guid="462d0ada-3716-5a42-af94-e242f09ca9f6",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Incineroar.Name",
    display_name="Incineroar",
    searchable_by=["Incineroar", "Stage 2", "Incineroar"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="SL",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    family_id=725,
    abilities=[
        Attack(
            title="Profane Punch",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 80 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=bonus_if(bench_has_damage, 80),
        ),
        Attack(
            title="Flare Blitz",
            game_text="Discard all Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            # STUB: attack effect not implemented
            effect=self_energy_discard_attack(all_energy=True, energy_type=PokemonTypes.FIRE),
        ),
    ],
)