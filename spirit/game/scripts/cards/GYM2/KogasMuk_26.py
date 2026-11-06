from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import energy_drain


card = PokemonCardDef(
    guid="5a9ceb17-a123-516a-b8c6-321a6cf04e24",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasMuk.Name",
    display_name="Koga's Muk",
    searchable_by=["Koga's Muk", "Stage 1", "KogasMuk"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="GYM2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KogasGrimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Energy Drain",
            game_text="If an opponent's attack does damage to Koga's Muk (even if Koga's Muk is Knocked Out), flip a coin. If heads and if it has any, choose 1 Energy card attached to the attacking Pok\u00e9mon and discard it. This power can't be used if Koga's Muk is already Asleep, Confused, or Paralyzed when your opponent attacks.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=energy_drain,
        ),
        Attack(
            title="Sludge Whirlpool",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
