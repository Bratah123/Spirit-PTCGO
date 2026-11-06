from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import HayFeverPassive, petal_whirlwind


card = PokemonCardDef(
    guid="b00d2943-c9f6-5984-9346-2103001187e5",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkVileplume.Name",
    display_name="Dark Vileplume",
    searchable_by=["Dark Vileplume", "Stage 2", "DarkVileplume"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Hay Fever",
            game_text="No Trainer cards can be played. This power stops working while Dark Vileplume is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=HayFeverPassive(),
        ),
        Attack(
            title="Petal Whirlwind",
            game_text="Flip a coins. This attack does 30 damage times the number of heads. If you get 2 or more heads, Dark Vileplume is now Confused (after doing damage).",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            damage_operator="x",
            effect=petal_whirlwind,
        ),
    ],
)
