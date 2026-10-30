from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import crushing_flames, legendary_ascent

card = PokemonCardDef(
    guid="c289dc5d-7613-55ee-a991-04e9e8fea644",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltresex.Name",
    display_name="Moltres ex",
    searchable_by=["Moltres ex", "Basic", "ex", "Moltresex"],
    subtypes=["Basic", "ex"],
    collector_number=115,
    set_code="EX6",
    rarity=Rarities.RareSecret,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=146,
    abilities=[
        Ability(
            title="Legendary Ascent",
            game_text="Once during your turn, when you put Moltres ex from your hand onto your Bench, you may switch 1 of your Active Pok\u00e9mon with Moltres ex. If you do, you may also move any number of basic Fire Energy cards attached to your Pok\u00e9mon to Moltres ex.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_PLAY,
            effect=legendary_ascent(),
        ),
        Attack(
            title="Crushing Flames",
            game_text="You may discard an Energy card attached to Moltres ex. If you do, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=crushing_flames(),
        ),
    ],
)