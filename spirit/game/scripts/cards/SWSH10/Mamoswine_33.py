from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    spread_damage, self_energy_discard_attack, lock_defender_attacks,
)


async def _iceberg_lock(ctx):
    lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="828361bc-84ac-503f-a608-3a22b66ce148",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mamoswine.Name",
    display_name="Mamoswine",
    searchable_by=["Mamoswine", "Stage 2", "Mamoswine"],
    subtypes=["Stage 2"],
    collector_number=33,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    family_id=220,
    abilities=[
        Attack(
            title="Blizzard",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=spread_damage(10, side="opponent", also_base=True),
        ),
        Attack(
            title="Iceberg Press",
            game_text="Discard an Energy from this Pok\u00e9mon. During your opponent's next turn, the Defending Pok\u00e9mon can't attack.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=self_energy_discard_attack(count=1, also=_iceberg_lock),
        ),
    ],
)