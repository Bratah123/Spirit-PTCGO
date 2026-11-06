from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import leek_slap, leek_slap_available


card = PokemonCardDef(
    guid="071b14f6-d26d-5e68-9ef7-5ef04ef34261",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farfetchd.Name",
    display_name="Farfetch'd",
    searchable_by=["Farfetch'd", "Basic", "Farfetchd"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=83,
    abilities=[
        Attack(
            title="Leek Slap",
            game_text="Flip a coin. If tails, this attack does nothing. Either way, you can't use this attack again as long as Farfetch'd stays in play (even putting Farfetch'd on the Bench won't let you use it again).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            condition=leek_slap_available,
            effect=leek_slap,
        ),
        Attack(
            title="Pot Smash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
