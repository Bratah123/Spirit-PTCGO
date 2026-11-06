from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import paint


card = PokemonCardDef(
    guid="049db089-5280-58a1-8287-62e31784c601",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=["Smeargle", "Basic", "Smeargle"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=235,
    abilities=[
        Attack(
            title="Paint",
            game_text="Flip a coin. If heads, choose a type (other than Colorless) and put a Coloring counter on the Defending Pok\u00e9mon. That Pok\u00e9mon is now the type you chose. If it already had a Coloring counter, remove the old one. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=paint,
        ),
    ],
)
