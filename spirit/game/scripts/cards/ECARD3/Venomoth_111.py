from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import healing_dust, miracle_tail


card = PokemonCardDef(
    guid="bc4b25cd-3159-569f-83a2-7e53556dd550",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venomoth.Name",
    display_name="Venomoth",
    searchable_by=["Venomoth", "Stage 1", "Venomoth"],
    subtypes=["Stage 1"],
    collector_number=111,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    family_id=48,
    abilities=[
        Attack(
            title="Healing Dust",
            game_text="Flip 2 coins. For each heads, remove 1 damage counter from each of your Pok\u00e9mon. If a Pok\u00e9mon has fewer damage counters than the number of heads, remove all of them.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=healing_dust,
        ),
        Attack(
            title="Miracle Powder",
            game_text="Flip a coin. If heads, choose a Special Condition (Asleep, Burned, Confused, Paralyzed, or Poisoned). The Defending Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=miracle_tail,
        ),
    ],
)
