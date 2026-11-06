from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    AntiLightningPassive, lightning_storm, plasma,
)


card = PokemonCardDef(
    guid="4a7d637d-5629-55ab-87ec-4ff1478f317f",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=182,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Ability(
            title="Anti-Lightning",
            game_text="You can't attach Lightning Energy cards from your hand to Zapdos.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=AntiLightningPassive(),
        ),
        Attack(
            title="Plasma",
            game_text="If there are any Lightning Energy cards in your discard pile, flip a coin. If heads, attach 1 of them to Zapdos.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=plasma,
        ),
        Attack(
            title="Lightning Storm",
            game_text="Flip a coin. If tails, put 2 damage counters on Zapdos.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=lightning_storm,
        ),
    ],
)
