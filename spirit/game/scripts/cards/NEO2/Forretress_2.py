from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import rapid_spin, spikes


card = PokemonCardDef(
    guid="26e13b94-989c-5bfc-897e-c376d8a7b0a6",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name",
    display_name="Forretress",
    searchable_by=["Forretress", "Stage 1", "Forretress"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="NEO2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Ability(
            title="Spikes",
            game_text="During your opponent's turn, whenever 1 of your opponent's Benched Pok\u00e9mon becomes his or her Active Pok\u00e9mon, Forretress does 10 damage to it. (Don't apply Weakness and Resistance.) This power stops working if Forretress is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_BENCH_TO_ACTIVE,
            effect=spikes,
        ),
        Attack(
            title="Rapid Spin",
            game_text="If your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with his or her Active Pok\u00e9mon, then, if you have any Benched Pok\u00e9mon, you switch 1 of them with your Active Pok\u00e9mon. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=rapid_spin,
        ),
    ],
)
