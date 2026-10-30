from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import optional_gust_then_damage, scam_supporter


card = PokemonCardDef(
    guid="d708e63a-f3f3-56e2-b848-e562d1311754",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic", "Mawile"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="EX2",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=303,
    abilities=[
        Attack(
            title="Scam",
            game_text="Look at your opponent's hand. You may have your opponent shuffle a Supporter card you find there into his or her deck. If you do, your opponent draws a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=scam_supporter,
        ),
        Attack(
            title="Metal Hook",
            game_text="Before doing damage, you may switch 1 of your opponent's Benched Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. If you do, this attack does 20 damage to the new Defending Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=optional_gust_then_damage(),
        ),
    ],
)
