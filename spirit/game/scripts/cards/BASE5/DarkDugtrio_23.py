from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import knock_down, sinkhole


card = PokemonCardDef(
    guid="827390ff-08fd-5a42-99dd-22f235f5e263",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkDugtrio.Name",
    display_name="Dark Dugtrio",
    searchable_by=["Dark Dugtrio", "Stage 1", "DarkDugtrio"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="BASE5",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    family_id=50,
    abilities=[
        Ability(
            title="Sinkhole",
            game_text="Whenever your opponent's Active Pok\u00e9mon retreats, your opponent flips a coin. If tails, this power does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance.) This power stops working while Dark Dugtrio is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_RETREAT,
            effect=sinkhole,
        ),
        Attack(
            title="Knock Down",
            game_text="Your opponent flips a coin. If tails, this attack does 20 damage plus 20 more damage; if heads, this attack does 20 damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            damage_operator="+",
            effect=knock_down,
        ),
    ],
)
