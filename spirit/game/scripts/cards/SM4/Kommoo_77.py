from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm4 import clanging_scales, war_cry

card = PokemonCardDef(
    guid="df1d9c4c-1642-5307-a7d6-4cab0872af1d",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kommoo.Name",
    display_name="Kommo-o",
    searchable_by=["Kommo-o", "Stage 2", "Kommoo"],
    subtypes=["Stage 2"],
    collector_number=77,
    set_code="SM4",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name",
    family_id=782,
    abilities=[
        Attack(
            title="War Cry",
            game_text="If you have fewer Pok\u00e9mon in play than your opponent, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=war_cry,
        ),
        Attack(
            title="Clanging Scales",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 more damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=clanging_scales,
        ),
    ],
)