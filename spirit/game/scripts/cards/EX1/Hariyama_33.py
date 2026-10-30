from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage


card = PokemonCardDef(
    guid="57a90d03-a000-5b28-8e20-ae8021e76c52",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name",
    display_name="Hariyama",
    searchable_by=["Hariyama", "Stage 1", "Hariyama"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    family_id=296,
    abilities=[
        Attack(
            title="Shove",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Slap Down",
            game_text="Flip 2 coins. This attack does 40 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=10),
        ),
    ],
)
