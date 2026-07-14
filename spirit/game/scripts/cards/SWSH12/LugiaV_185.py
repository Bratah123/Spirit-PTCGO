from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import read_the_wind, aero_dive

card = PokemonCardDef(
    guid="8f37693b-3a5b-5518-92f1-285083214ff7",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LugiaV.Name",
    display_name="Lugia V",
    searchable_by=["Lugia V", "Basic", "V", "LugiaV"],
    subtypes=["Basic", "V"],
    collector_number=185,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Attack(
            title="Read the Wind",
            game_text="Discard a card from your hand. If you do, draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=read_the_wind,
        ),
        Attack(
            title="Aero Dive",
            game_text="You may discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            effect=aero_dive,
        ),
    ],
)