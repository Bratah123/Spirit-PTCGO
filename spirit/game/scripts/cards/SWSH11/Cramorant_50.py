from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import LostProvisionsPassive, spit_innocently

card = PokemonCardDef(
    guid="617f36e9-cdfd-5ea6-a0c6-1d1bf83d8087",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cramorant.Name",
    display_name="Cramorant",
    searchable_by=["Cramorant", "Basic", "Cramorant"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=845,
    abilities=[
        Ability(
            title="Lost Provisions",
            game_text="If you have 4 or more cards in the Lost Zone, ignore all Energy in this Pok\u00e9mon's attack costs.",
            passive=LostProvisionsPassive(),
        ),
        Attack(
            title="Spit Innocently",
            game_text="This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=spit_innocently,
        ),
    ],
)
