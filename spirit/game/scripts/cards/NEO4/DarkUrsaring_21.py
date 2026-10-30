from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import battle_frenzy, provoke


card = PokemonCardDef(
    guid="8ddb0501-7a4f-5f83-aef1-282da4c14eab",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkUrsaring.Name",
    display_name="Dark Ursaring",
    searchable_by=["Dark Ursaring", "Stage 1", "DarkUrsaring"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    family_id=217,
    abilities=[
        Attack(
            title="Provoke",
            game_text="Look at your opponent's hand. If he or she has any Baby Pok\u00e9mon and/or Basic Pok\u00e9mon there, you may put any number of them onto your opponent's Bench (as long as there's room). Then, your opponent looks at your hand. If you have any Baby Pok\u00e9mon and/or Basic Pok\u00e9mon there, your opponent may put any number of them onto your Bench (as long as there's room).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=provoke,
        ),
        Attack(
            title="Battle Frenzy",
            game_text="For each Pok\u00e9mon in play (yours and your opponent's), flip a coin. For each heads, this attack does 20 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance for this attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=battle_frenzy,
        ),
    ],
)
