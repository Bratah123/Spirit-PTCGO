from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import delayed_knockout, read_the_wind

card = PokemonCardDef(
    guid="8cacaf2d-8771-56d9-9dc6-22313137a545",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowkingV.Name",
    display_name="Galarian Slowking V",
    searchable_by=["Galarian Slowking V", "Basic", "V", "Single Strike", "GalarianSlowkingV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=99,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=199,
    abilities=[
        Attack(
            title="Concoction",
            game_text="Discard a card from your hand. If you do, draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=read_the_wind,
        ),
        Attack(
            title="Word of Ruin",
            game_text="At the end of your opponent's next turn, the Defending Pok\u00e9mon will be Knocked Out.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=delayed_knockout,
        ),
    ],
)