from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import exoskeleton_20_passive, flip_damage_paralyze_on_heads


card = PokemonCardDef(
    guid="4723b453-6f66-52cd-ad5d-3c1249b1a21d",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cloyster.Name",
    display_name="Cloyster",
    searchable_by=["Cloyster", "Stage 1", "Cloyster"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="EX6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name",
    family_id=90,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="Any damage done to Cloyster by attacks is reduced by 20 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=exoskeleton_20_passive(),
        ),
        Attack(
            title="Double Bubble",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads. If either of the coins is heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=flip_damage_paralyze_on_heads(coins=2, per_heads=10),
        ),
        Attack(
            title="Shell Attack",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)