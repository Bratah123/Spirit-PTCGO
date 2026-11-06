from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    AntiFirePassive, collect_energy_from_discard, fireworks,
)


card = PokemonCardDef(
    guid="45234d60-ea75-5339-a2b7-9f27b241ce15",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=170,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=146,
    abilities=[
        Ability(
            title="Fire Immunity",
            game_text="You can't attach Fire Energy cards from your hand to Moltres.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=AntiFirePassive(),
        ),
        Attack(
            title="Collect Fire",
            game_text="If there are any Fire Energy cards in your discard pile, flip a coin. If heads, attach 1 of them to Moltres.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=collect_energy_from_discard(PokemonTypes.FIRE),
        ),
        Attack(
            title="Burning Tail",
            game_text="Flip a coin. If tails, discard a Fire Energy card attached to Moltres.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=fireworks,
        ),
    ],
)
