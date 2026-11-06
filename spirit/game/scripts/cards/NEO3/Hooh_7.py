from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing, snipe_attack
from spirit.game.card_effects.ecard import stoke


card = PokemonCardDef(
    guid="25ff4c77-b907-5811-912a-4281811ea431",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hooh.Name",
    display_name="Ho-oh",
    searchable_by=["Ho-oh", "Basic", "Hooh"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Attack(
            title="Stoke",
            game_text="You may search your deck for a Fire Energy card and attach it to Ho-Oh. Shuffle your deck afterward.",
            cost={PokemonTypes.FIRE: 1},
            effect=stoke,
        ),
        Attack(
            title="Sacred Fire",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.FIRE: 3},
            effect=flip_or_nothing(
                then=snipe_attack(40, pool="any", apply_modifiers=False)),
        ),
        Attack(
            title="Dive Bomb",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIRE: 5},
            damage=90,
            effect=flip_or_nothing(),
        ),
    ],
)
